

def addNewUser(dataset, name, email, age):

    dataset[email]= \
        {
            "personal_info": {
                "name": name,
                "age": age
            },
            "orders":
                {

                }

        }
    return  dataset[email]


def addNewOrder(dataset, email, date, shop):
    dataset[email]["orders"][date] =\
                    {
                        "shop": shop,
                        "products": {

                                    }
                    }
    return dataset[email]["orders"][date]



def addProductToOrder(dataset, email, date, product_name, product_weight, product_price):
    dataset[email]["orders"][date]["products"][product_name] = \
        {
            "weight": product_weight,
            "price_per_kilo": product_price

        }