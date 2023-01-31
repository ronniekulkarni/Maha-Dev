from product_services import ProductServices
from product_info import Product


class ProductServiceImpl(ProductServices):

    product_list = []     #only products          #class variable

    def add_product(self,prod):
        if type(prod)==Product:         # checking  prod object-- kontay type cha ahe product type
            if prod.prod_id>0:              # prodid valid ahe ka --> valid means >0
                if prod.prod_price>0:           #*
                    ProductServiceImpl.product_list.append(prod)
                    print('Product Successfully Added..')
                else:
                    print('Invalid Product Price..!')
            else:
                print('Invalid Product Id..!')
        else:
            print('Invalid product Type...cannot be added...!')

    def update_product(self,pid,newvalues):
        if not type(newvalues) == Product:
            print('Invalid Product Type..')

        for prod in ProductServiceImpl.product_list:
            if prod.prod_id == pid:
                prod.prod_name = newvalues.prod_name
                prod.prod_price = newvalues.prod_price
                prod.prod_qty = newvalues.prod_qty
                prod.prod_vendor = newvalues.prod_vendor
                prod.prod_category = newvalues.prod_vendor
                print('Product Successfully Updated...')
                return      # caller kade..
        else:
        print('Product with given details not found...so cannot update')


    def delete_product(self,pid):
        if pid>0:
            for prod in ProductServiceImpl.product_list:
                if prod.prod_id == pid:
                    ProductServiceImpl.product_list.remove(prod)
                    print('Product Successfully Deleted..')
                    break
        else:
            print('Invalid Product id..!')


    def delete_all_product(self, pid):
        if pid > 0:
            for prod in ProductServiceImpl.product_list:
                if prod.prod_id == pid:
                    ProductServiceImpl.product_list.remove(prod)
                    print('Product Successfully Deleted..')
                    #break
        else:
            print('Invalid Product id..!')

    def search_product(self,pid):
        if pid > 0:
            for prod in ProductServiceImpl.product_list:
                if prod.prod_id == pid:
                    #ProductServiceImpl.product_list.remove(prod)
                    #print('Product Successfully Deleted..')
                    return prod  # caller kade.. --> product gheun --> id match zalela
        else:
            print('Invalid Product id..!')

    def max_price_product(self):
        max_price = 0.0
        for prod in ProductServiceImpl.product_list:
            if prod.prod_price>max_price:
                max_price = prod.prod_price
        print('This is Maximum Price --> ',max_price)

    def min_price_product_v1(self):
        ProductServiceImpl.product_list.sort(key=lambda item: item.prod_price)
        return ProductServiceImpl.product_list[0].prod_price


    def min_price_product(self):
        min_price = ProductServiceImpl.product_list[0].prod_price
        for prod in ProductServiceImpl.product_list:
            if prod.prod_price < min_price:
                min_price = prod.prod_price


        print('This is Min Price --> ', min_price)
        return min_price

    def min_price_product_all(self):
        # min_price = ProductServiceImpl.product_list[0].prod_price
        # for prod in ProductServiceImpl.product_list:
        #     if prod.prod_price < min_price:
        #         min_price = prod.prod_price
        # print('This is Min Price --> ', min_price)
        min_price = self.min_price_product()
        temp_list = []
        for prod in ProductServiceImpl.product_list:
            if prod.prod_price == min_price:
                temp_list.append(prod)

        return temp_list

    def product_in_price_range(self,start_range,end_range):
        temp_list = []

        for prod in ProductServiceImpl.product_list:
            if prod.prod_price>=start_range and prod.prod_price<=end_range:
                temp_list.append(prod)

        return temp_list

    def avg_product_price(self):
        result = 0.0
        for prod in ProductServiceImpl.product_list:
            result = result + prod.prod_price

        print('Total Price of Products..',result)
        avg_price = result/len(ProductServiceImpl.product_list)
        print('Avg Price of Products..', avg_price)

    def list_products(self):
        return ProductServiceImpl.product_list

    def list_by_category(self,category):
        templist = []
        for prod in ProductServiceImpl.product_list:
            if prod.prod_category == category:
                templist.append(prod)

        return templist