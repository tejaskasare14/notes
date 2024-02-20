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

//creating flipkart db and product as collection
//create database flipkacrt;
use('flipkart')

//create table quesry in sql
//db.createCollection('products')

//get names of all collection in selected db (flipkart)
//show tables;
//db.getCollectionNames()

//inserting one record inside products collection
db.products.insertOne(
   {{name:'iphone',price:200,quantity:5,colors:['red','black'],dimension:{w:10,h:20,unit:'cm'}},}
)





















