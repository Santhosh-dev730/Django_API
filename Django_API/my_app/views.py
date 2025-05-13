from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *

# Create your views here.
class ProductsView(APIView):

    def post(self,request):

        print(request.data) # api -> postman -> create a object like {} like key -> double quotes 

        new_product = Product(product_name = request.data['product_name'], code = request.data['code'], price = request.data['price'])
        new_product.save()

        return Response("Data Saved")

    # def get(self,request):

    #     products_data = Product.objects.all()
    #     all_products = []
    #     for product in products_data:

    #         single_product = {
    #             'id': product.id,
    #             'product_name': product.product_name,
    #             'code': product.code,
    #             'price': product.price,
    #         }
    #         print(single_product)
    #         all_products.append(single_product)
    #     return Response(all_products)

    
    # Using Serializers 
    def get(self,request):

        products_data = Product.objects.all()
        
        serialized_product = Product_Serializers(products_data, many=True).data

        return Response(serialized_product)


    def delete(self,request,id):

        delete_obj = Product.objects.get(id=id)
        delete_obj.delete()
        return Response("Deleted")
    

    def patch(self, request, id):
        selected_product = Product.objects.filter(id = id)

        selected_product.update(product_name = request.data['product_name'], code = request.data['code'], price = request.data['price'])

        return Response("Selected Product is updated")

