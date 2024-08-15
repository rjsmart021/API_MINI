from flask_marshmallow import Marshmallow
from marshmallow import fields, validate
from API_MINI import app

ma = Marshmallow()


from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Bakery(db.Model):
    __tablename__ = 'Bakery'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
# schema.py
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models import Bakery as BakeryModel, Product as productModel, product_genres, db
from sqlalchemy.orm import Session

class Bakery(SQLAlchemyObjectType):
    class Meta:
        model = BakeryModel

class product(SQLAlchemyObjectType):
    class Meta:
        model = productModel

class Query(graphene.ObjectType):
    Bakery = graphene.List(Bakery)
    search_Bakery = graphene.List(Bakery, title=graphene.String(), director=graphene.String(), year=graphene.Int())
    get_Bakery_by_product = graphene.List(Bakery, product_id=graphene.Int())
    get_product_by_Bakery = graphene.List(Product, Bakery_id=graphene.Int())

    def resolve_Bakery(root, info):
        return db.session.execute(db.select(BakeryModel)).scalars()

    def resolve_search_bakery(root, info, title=None, director=None, year=None):        
        query = db.select(BakeryModel)
        if title:
            query = query.where(BakeryModel.title.ilike(f'%{title}%'))
        if director:
            query = query.where(BakeryModel.director.ilike(f'%{director}%'))
        if year:
            query = query.where(BakeryModel.year == year)
        results = db.session.execute(query).scalars().all()
        return results
    
    def resolve_get_bakery_by_product(root, info, genre_id):
        return db.session.query(BakeryModel).join(bakery_product).filter(bakery_product.c.bakery_id == product_id).all()

    def resolve_get_product_by_bakery(root, info, bakery_id):
        return db.session.query(ProductModel).join(bakery_product).filter(bakery_product.c.bakery_id == bakery_id).all()
    
class Addbakery(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        director = graphene.String(required=True)
        year = graphene.Int(required=True)
        genres = graphene.List(graphene.String, required=True)

    movie = graphene.Field(Bakery)

    def mutate(root, info, title, director, year, genres):

        # get genres from table, or add them if necessary
        genre_instances = []
        for product_name in products:
            product_instance = db.session.query(procuctModel).filter_by(name=product_name).first()
            if not product_instance:
                product_instance = ProductModel(name=genre_name)
            product_instances.append(product_instance)

        Bakery = bakeryModel(Name=Name, price=price, ItemID=ItemID, Calorie=Calorie) 
        return AddBakery(bakery=bakery)

class Updatebakery(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        title = graphene.String()
        director = graphene.String()
        year = graphene.Int()
        genres = graphene.List(graphene.String, required=True)

    bakery = graphene.Field(Bakery)

    def mutate(root, info, id, Name=None, Price=None, ItemID=None, Calorie=None):
        bakery = db.session.get(BakeryModel, id)         
        if not bakery:
            return None
        if name:    
            bakery.name = name
        if price:
            bakery.price = price
        if year:
            bakery.ItemID = ItemID
        if product:
            product_instances = []
            for product_name in products:
                product_instance = db.session.query(ProductModel).filter_by(name=product_name).first()
                if not product_instance:
                    product_instance = ProductModel(name=product_name)
                product_instances.append(product_instance)
            bakery.products = product_instances
        db.session.commit()
        return UpdateBakery(product=prouct)

class DeleteBakery(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    message = graphene.String()

    def mutate(root, info, id):
        movie = db.session.get(BakeryModel, id)         
        if not bakery:
            return DeleteBakery(message="That bakery was not found")
        else:
            db.session.delete(bakery)
            db.session.commit()
            return DeleteBakery(message="Success")


### Product MUTATIONS ###

class AddProduct(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    genre = graphene.Field(Product)

    def mutate(root, info, name):
        product = ProductModel(name=name)
        return AddProduct(product=product)

class UpdateProduct(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String()

    product = graphene.Field(Product)

    def mutate(root, info, id, name=None):
        product = db.session.get(ProductModel, id)         
        if not product:
            return None
        if name:    
            product.name = name
        db.session.commit()
        return UpdateProductproduct=product)

class DeleteProduct(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    message = graphene.String()

    def mutate(root, info, id):
        genre = db.session.get(ProductModel, id)         
        if not genre:
            return DeleteProduct(message="That genre was not found")
        else:
            db.session.delete(product)
            db.session.commit()
            return DeleteProduct(message="Success")


class Mutation(graphene.ObjectType):
    create_movie = AddBakery.Field()
    update_movie = UpdateBakery.Field()
    delete_movie = DeleteBakery.Field()
    create_genre = AddProduct.Field()
    update_genre = UpdateProduct.Field()
    delete_genre = DeleteProduct.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

ma.init_app(app)
