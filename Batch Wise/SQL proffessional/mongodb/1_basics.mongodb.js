//show databases;
//db.getMongo().getDBs();

//how to create and delete database and collection in mongo
//use('test_db');
//db.getMongo().getDBs();

//we cant create database just by writting use()
//we have to compulsory create collection inside db
//therefor run below 2 lines at once
// use('test_db');
// db.createCollection('test_collection')

//db.getMongo().getDBs(); 

//below run 17 and 18 at once then 17 and 19 at once
//use('test_db');
//db.test_collection.drop();
//db.dropDatabase();

//----creating flipkart db and product as collection
//----create database flipkacrt;
use('flipkart'); //do not comment this line

//----create table quesry in sql
//db.createCollection('products');

//----get names of all collection in selected db (flipkart)
//----show tables;
//db.getCollectionNames();

//----inserting one record inside products collection
//db.products.insertOne(
//    {name:'iphone',price:200,quantity:5,colors:['red','black'],dimension:{w:10,h:20,unit:'cm'}}
// );

//----getting all data from products
//select * from products;
//db.products.find();


//----inserting multiple records inside products collection
// db.products.insertMany(
//    [
// {name:'tv',price:350,quantity:10,colors:['black','red'],dimension:{w:45,h:30,unit:'in'}},
// {name:'book',price:150,quantity:15,colors:['red','black','blue'],dimension:{w:10,h:15,unit:'in'}},
// {name:'notebook',price:100,quantity:5,colors:['yellow','black'],dimension:{w:10,h:15,unit:'cm'}},
// {name:'pen',price:50,quantity:100,colors:['blue','green'],dimension:{w:5,h:10,unit:'cm'}}
//    ]
// );



//select * from products;
//db.products.find();

//select * from products where quantity=5
// db.products.find(
//    {quantity:5}
// );

//select * from products where quantity>5
db.products.find(
   // {quantity:{$gt:5}}
   {quantity:{$gte:5}}
);





















