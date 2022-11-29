from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from rest_framework import status
from .models import kicks
from django.conf import settings
from .serializers import kicksSerializer
import pprint
import requests
import json
import urllib.request as req
from urllib.parse import urlparse
import chardet
import os
import time
import shutil
from yarl import URL
from google_images_download import google_images_download   #importing the library



'''
returns 15 most recent drops (no paginations) -> for main page component
'''
def popular_release(request):
    if request.method == 'GET':
        product_list = kicks.objects.exclude(local_imageUrl='http://localhost:8000/media/images/defaultImg.png').order_by('-releaseDate')[0:12]
        
        serializer = kicksSerializer(product_list, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
    
'''
메인 페이지용, 신제품 선택 def
최근 등록된 15개 중 사진 file 을 가지고있고, 그중 기대 리셀가가 가장 높은 제품 1종 Return 
'''
def main_img(request):
    if request.method == 'GET':
        product_list = kicks.objects.exclude(local_imageUrl='http://localhost:8000/media/images/defaultImg.png').order_by('-releaseDate', '-estimatedMarketValue')[:25]
        main_img = product_list[0]
        result = []
        for p in product_list:
            if main_img.estimatedMarketValue < p.estimatedMarketValue:
                main_img = p
                result.append(main_img)
        print(f'main_img : {result}')
        serializer = kicksSerializer(result[:2], many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)



'''
sneaker list v.0.1
TODO: Searching function needs to be added. 
'''
def get_sneaker(request): 
    page = request.GET.get("page")
    sneaker_list = kicks.objects.all().order_by('-releaseDate')
    paginator = Paginator(sneaker_list, 20)
    sneakers = paginator.get_page(page)
    serializer = kicksSerializer(sneakers, many=True)
    print(f'res : {sneakers}')
    
    return JsonResponse(serializer.data, safe=False)

def get_detail(request):
    kick = get_object_or_404(kicks, id=request.GET.get('id'))
    
    serializer = kicksSerializer(kick)
    print(f'res : {kick}')
    
    return JsonResponse(serializer.data, safe=False)



'''
sneakers Data paser v1.0.0

'''
pp = pprint.PrettyPrinter(indent=4)
headers = {
    'accept': 'application/json',
    'accept-encoding': 'utf-8',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'Origin': 'https://thesneakerdatabase.com',
    'app-platform': 'Iron',
    'Host': 'www.thesneakerdatabase.com',
    'referer': 'https://stockx.com/en-gb',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.62 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}

new_release_url = getattr(settings, 'NEW_RELEASE_URL', None)



def create_new_kick_data(products_list, p):
    try:
        kick = kicks.objects.get(sku=products_list[p]['sku'])
        print('Already exists')
        # 이미 등록된 제품이지만, 이미지 파일 업데이트 확인 

        if products_list[p]['image']['original'] != '' and kick.imageUrl == '':
            print('product image updated')
            kick.imageUrl      = products_list[p]['image']['original']
            kick.smallImageUrl = products_list[p]['image']['small']
            kick.thumbUrl      = products_list[p]['image']['thumbnail']

            kick.save()
            
            return 1
        
        return 0
    except kicks.DoesNotExist: # 존재하지 않는 제품이므로, 등록 처리
        #TODO: 신제품 등록시 사진 파일도 저장 처리 
        print('New product')
        kick = kicks(
                    uuid                 = products_list[p]['_id'],
                    brand                = products_list[p]['brand'],
                    colorway             = products_list[p]['colorway'],                    
                    gender               = products_list[p]['gender'],
                    description          = products_list[p]['story'],
                    name                 = products_list[p]['name'],
                    releaseDate          = products_list[p]['releaseDate'],
                    retailPrice          = products_list[p]['retailPrice'],
                    estimatedMarketValue = products_list[p]['estimatedMarketValue'],
                    sku                  = products_list[p]['sku'],
                    imageUrl             = products_list[p]['image']['original'],
                    smallImageUrl        = products_list[p]['image']['small'],
                    thumbUrl             = products_list[p]['image']['thumbnail'],
            )
        kick.save()
        
        return 1 



def new_release_paser(request):
    
    response = requests.get(url=new_release_url, headers=headers)
    print('res: ', response.status_code)
    json_data = json.loads(response.text)
    products_list = json_data['data']
    new_cnt = 0
    
    for p in range(len(products_list)):
        new_cnt += create_new_kick_data(products_list, p)
    print(f'new Count = {new_cnt}')
    return HttpResponse(status= status.HTTP_201_CREATED)



def sneaker_datasneaker_data_by_year_paser_by_brand_paser(request):
    
    response = requests.get(url=new_release_url, headers=headers)
    json_data = json.loads(response.text)
    products_list = json_data['data']
    
    for p in range(len(products_list)):
        create_new_kick_data(products_list, p)

    return HttpResponse(status= status.HTTP_201_CREATED)



def sneaker_data_by_brand_paser(request):
    j_url_m = getattr(settings, 'J_URL_M', None)
    j_url_f = getattr(settings, 'J_URL_F', None)
    n_url_m = getattr(settings, 'N_URL_M', None)
    n_url_f = getattr(settings, 'N_URL_M', None)
    

    cnt = 0
    response = requests.get(url=n_url_f, headers=headers)
    json_data = json.loads(response.text)
    products_list = json_data['data']
    
    for p in range(len(products_list)):
        cnt += create_new_kick_data(products_list, p)
    
    print(f'new Count : {cnt}')
    
    return HttpResponse(status= status.HTTP_201_CREATED)


#update Count : 4849
def sneaker_img_paser(request):
    start = time.time()
    # 이미 추가한 것 필터로 빼고 갖고오기..
    all_products = kicks.objects.filter(local_imageUrl='http://localhost:8000/media/images/defaultImg.png').order_by('-releaseDate')
    
    for i, p in enumerate(all_products):
        if p.imageUrl!='' and p.imageUrl.find('stockx')== -1:
            print(f'Name check (goat): {p.name}')
            imageUrl = p.imageUrl
            # path = os.path.dirname(imageUrl)[22:]
            # 저장 경로 
            file_name = os.path.basename(imageUrl)
            path = urlparse(imageUrl).path
            path_url = path[:path.find(file_name)]
            
            
            local_path = '/Users/isaac/Desktop/Project/culturesupply/media/images/sneakers'+path_url
            # print(f'path check : {local_path}')
            # 저장 할 제품 이름
            # 디렉토리가 없으면 생성
            # check_dir(local_path)
            # 설정한 경로에 파일 저장 
            req.urlretrieve(imageUrl, '/Users/isaac/Desktop/Project/culturesupply/media/images/sneakers/'+file_name)
            # 해당 제품 db 업데이트
            img_url = 'http://localhost:8000/media/images/sneakers/'+file_name
            p.local_imageUrl = img_url
            ################################################################################################
            smallImageUrl = p.smallImageUrl
            # 저장 할 제품 이름
            file_name = os.path.basename(smallImageUrl)
            path = urlparse(smallImageUrl).path
            path_url = path[:path.find(file_name)]
            # 저장 경로 
            local_path = '/Users/isaac/Desktop/Project/culturesupply/media/images/sneakers'+path_url
            # 디렉토리가 없으면 생성
            # check_dir(local_path)
            # 설정한 경로에 파일 저장 
            req.urlretrieve(smallImageUrl, '/Users/isaac/Desktop/Project/culturesupply/media/images/sneakers/'+file_name)
            # 해당 제품 db 업데이트
            small_img_url = 'http://localhost:8000/media/images/sneakers/'+file_name
            p.local_smallImageUrl = small_img_url
            ################################################################################################
            thumbUrl = p.thumbUrl
           # 저장 할 제품 이름
            file_name = os.path.basename(thumbUrl)
            path = urlparse(thumbUrl).path
            path_url = path[:path.find(file_name)]
            # 저장 경로 
            local_path = '/Users/isaac/Desktop/Project/culturesupply/media/images/sneakers'+path
            # 디렉토리가 없으면 생성
            # check_dir(local_path)
            # 설정한 경로에 파일 저장 
            req.urlretrieve(thumbUrl, '/Users/isaac/Desktop/Project/culturesupply/media/images/sneakers/'+file_name)
            # 해당 제품 db 업데이트
            thumb_Url_img_url = 'http://localhost:8000/media/images/sneakers/'+file_name

            p.local_thumbUrl = thumb_Url_img_url
            # 최종 저장 
            p.save()
            print(f'update Count : {i}')
        # Stockx url 일 경우, 
        elif p.imageUrl!='' and p.imageUrl.find('stockx') >= 0:
            print(f'Name check (stockX) : {p.name}')
            opener = req.build_opener()
            opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
            
            req.install_opener(opener)
            # encode : {'encoding': 'Windows-1252', 'confidence': 0.73, 'language': ''}
            print(f'encode : {chardet.detect(p.imageUrl.encode())}')
            imageUrl = p.imageUrl
            
            file_name = os.path.basename(imageUrl)
            path = urlparse(imageUrl).path
            path_url = path[:path.find(file_name)]
            # 저장 경로 
            local_path = '/Users/isaac/Desktop/Project/culturesupply/media/images/sneakers'+path
            # 저장 할 제품 이름
            file_name = os.path.basename(imageUrl)
            # 디렉토리가 없으면 생성
            # check_dir(local_path)
            # 설정한 경로에 파일 저장 
            req.urlretrieve(imageUrl, '/Users/isaac/Desktop/Project/culturesupply/media/images/sneakers/'+file_name[:file_name.find('?')])
            # 해당 제품 db 업데이트
            img_url = 'http://localhost:8000/media/images/sneakers/'+file_name[:file_name.find('?')]
            p.local_imageUrl = img_url
            p.save()
            print(f'update Count : {i}')
    print(time.time() - start)
    return HttpResponse(status= status.HTTP_200_OK)

def check_dir(local_path):
    try : 
        if not os.path.exists(local_path):
            os.makedirs(local_path)
    except OSError:
        print(OSError.strerror)

def google_img_download(request):
    all_products = kicks.objects.filter(imageUrl='').order_by('-releaseDate')
    
    for p in all_products:
        response = google_images_download.googleimagesdownload()   #class instantiation
        arguments = {"keywords":p.name,
                    "limit":1,
                    "print_urls":True,
                    # "specific_site": "stockx.com/",
                    "image_directory": "images/sneakers/",
                    "output_directory": "media/"
                    }   
        
        try:
            paths = response.download(arguments)  
            
            raw_url = paths[0][list(paths[0].keys())[0]]

            print(f'final check2 : {"http://localhost:8000" + raw_url[0][raw_url[0].find("/media"):]}') #
            p.local_imageUrl = "http://localhost:8000" + raw_url[0][raw_url[0].find("/media"):]
            p.save()
                
        except Exception as error:
            print(f'error : {error}')
            continue

    
    return HttpResponse(status.HTTP_201_CREATED)