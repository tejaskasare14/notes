//creating database and table(collection)
//run below 2 commands at a time
//use('amazon');
//db.createCollection('products');

//----------------------------------------------------
//deleting database and collection
//use('dummy_db');
//db.createCollection('dummy_collection');

//dropping collection
//db.dummy_collection.drop()

//deropping databse
//db.dropDatabase()
//-------------------------------------------------------

//to get current database
//db; //test is default database given by mongodb

//use is used to switch database
use('amazon');


//getting name of collections/table from selected database
//db.getCollectionNames();


//getting list of all databases;
//db.getMongo().getDBs();

//insert 1 record into products
// db.products.insertOne(
//    {name:'iphone',price:200,quantity:5,colors:['red','black'],dimension:{w:10,h:20,unit:'cm'}},
// )

//insert mulitple record into products
//  db.products.insertMany(
//    [
//       {name:'tv',price:350,quantity:10,colors:['black','red'],dimension:{w:45,h:30,unit:'in'}},
//       {name:'book',price:150,quantity:15,colors:['red','black','blue'],dimension:{w:10,h:15,unit:'in'}},
//       {name:'notebook',price:100,quantity:5,colors:['yellow','black'],dimension:{w:10,h:15,unit:'cm'}},
//       {name:'pen',price:50,quantity:100,colors:['blue','green'],dimension:{w:5,h:10,unit:'cm'}}
//    ]
// )



//select * from products;
//db.products.find()

//select * from products where quantity = 5;
// db.products.find(
//    {quantity:5}
// )

//select * from products where quantity = 5 limit 1; 
// db.products.findOne(
//    {quantity:5}
// )

//inserting one record without all fields 
// db.products.insertOne(
//    {name:'chair',quantity:8}
// )


//inserting one record with diff fields 
// db.products.insertOne(
//    {gender:'m',city:'pune'}
// )

// ---------------------  UPDATE  ------------------------------------------------------
//update products set quantity=10 where name=chair
//db.products.updateOne({name:'chair'},{ $set:{quantity:10}})
//db.products.find()

//update products set quantity=10,price=250 where name=chair
//here we can add last modified date for future use
//db.products.updateOne(
//    {name:'chair'},
//    { $set:{quantity:10,price:250}, $currentDate:{lastModifiedDate:true}}
// )
//db.products.find()

// ----------------------------------- DELETE --------------------------------
//delete from products where gender = m
// db.products.deleteOne(
//    {gender:'m'}
// )

//db.products.find()

//deleting based in id
//65c7592b51069dbde24873c2 copy the _id of chair
// db.products.deleteOne(
//    {  _id : ObjectId('65c7592b51069dbde24873c2')}
// )

//db.products.find()












