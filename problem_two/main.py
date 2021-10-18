
#
# Please check Readme for instructions on how to run this project



from pymongo import MongoClient
client = MongoClient()
client = MongoClient('mongodb://localhost:27017/')

# Access database
mydatabase = client['DominosDB']


def create_customer(name, num_goods_bought, id):
    if(not(type(name) == str)):
        raise TypeError('Name of customer should be a string')

    if(not(type(num_goods_bought) == int)):
        raise TypeError('Number of goods bought should be an integer.')

    if (not (type(id) == int)):
        raise TypeError('Customer ID should be an integer.')

    query = {'id': id }

    customer = mydatabase.customer_info.find_one(query)

    if(not(customer == None)):
        raise ValueError('Person with this id already exists. Please enter a diff id')

    rec = {
        'name': name,
        'num_goods': num_goods_bought,
        'id': id
    }
    mydatabase.customer_info.insert_one(rec)



def create_order(customer_id):

    query = {'id' : customer_id}

    customer = mydatabase.customer_info.find_one(query)

    if customer == None:
        raise ValueError('A customer with this id does not exist')

    num_goods = customer['num_goods'] + 1
    new_values = {'$set': {'num_goods': num_goods}}
    mydatabase.customer_info.update_one(query, new_values)

    order = {
        'customer_id': customer_id,
        'num_goods': num_goods
    }

    mydatabase.orders.insert_one(order)

def retrieve_customers():
    customers = []

    for customer in mydatabase.customer_info.find():
        customers.append(customer)

    return customers






