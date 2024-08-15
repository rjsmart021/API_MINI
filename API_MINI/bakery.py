from flask import jsonify, request

from API_MINI import app
from API_MINI.models import bakery
from API_MINI import db
from API_MINI.schemas import bakerySchema

bakery_schema = bakerySchema()


@app.route('/bakery', methods=['POST'])
def add_bakery():
    """
    Add bakery . Example POST data format
    {
    "bakery_name": "abc",
    "Prouct": "abc",
    :Quantity": "abd"
    }
    :return: success or error message
    """
    try:
        data = request.get_json()
        errors = bakery_schema.validate(data)
        if errors:
            return jsonify(errors), 400
        products = data.get("bakery")
        customers = data.get("customer")
        # Check if the bakery already exists based on Artist_name or Record_lable
        existing_bakery = bakery.query.filter(
            (bakery.products == products) | (bakery.customers == customers)
        ).first()

        if existing_bakery:
            return jsonify({"message": f"bakery already existed"})
        products = product(product=data["product_name"], Customer=data["Customer"],
                            customer=data["customer"])

        # Add the new customer to the database
        db.session.add(bakery)
        db.session.commit()

        return jsonify({"message": "bakery added successfully"})
    except Exception as e:
        return jsonify({"Error": f"bakery not added. Error {e}"})


@app.route('/bakery/<int:customer_id>', methods=['GET'])
def get_bakey(bakery_id):
    """
    Get bakery data based on ID provided
    :param bakery_id: ID of the registered Song.
    :return: customer details oif found else Error message
    """
    try:
        Song = bakery.query.get(bakery_id)

        if bakery:
            bakery_data = {
                "bakery_id": bakery.bakery_id,
                "bakery_name": bakery.bakery_name,
                "product": product.Product_name,
                "Customer": bakery.customer
            }
            return jsonify(bakery_data)
        else:
            return jsonify({"message": "bakery not found"})

    except Exception as e:
        print(f"Error in getting bakery. Error Message: {e}")
        return jsonify(
            {"message": f"Error while fetching bakery with ID: {bakery_id}. Error: {e}"})


@app.route('/bakery/<int:bakery_id>', methods=['PUT'])
def update_user(bakery_id):
    """
    Update the bakery details.
    example PUT data to update;
    {
    "bakery_name": "name",
    "product": "product",
    "customer": "customer"
    }
    :param bakery_id:
    :return:
    """
    try:
        bakery = bakery.query.get(bakery_id)

        if bakery:
            data = request.get_json()
            error = bakery_schema.validate(data)
            if error:
                return jsonify(error), 400
            bakery.bakery_name = data.get('bakery_name', bakery.bakery_name)
            bakery.Product = data.get('Product', Product.Product)
            bakery.Customer = data.get('Customer_ID', Customer.Customer)

            db.session.commit()
            return jsonify({"message": "bakery updated successfully"})
        else:
            return jsonify({"message": "bakery Not Found!!!"})
    except Exception as e:
        return jsonify({"message": f"error in updating bakery. Error: {e}"})


@app.route('/bakery/<int:bakery_id>', methods=['DELETE'])
def delete_user(bakery_id):
    """
    Delete user based on the ID provided
    :param bakery_id: ID of the bakery to delete
    :return: success message if user deleted successfully else None
    """

    try:
        bakery = bakery.query.get(bakery_id)

        if bakery:
            # Delete the bakery from the database
            db.session.delete(bakery)
            db.session.commit()
            return jsonify({"message": "bakery deleted successfully"})
        else:
            return jsonify({"message": "bakery not found"})

    except Exception as e:
        return jsonify({"message": f"error in deleting bakery. Error: {e}"})
