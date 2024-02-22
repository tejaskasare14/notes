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
// db.products.find(
//    // {quantity:{$gt:5}}
//    {quantity:{$gte:5}}
// );

//inserting record without all fields
// db.products.insertOne(
//    {name:'chair',quantity:5}
// );

//db.products.find();

//inserting record with diff fields
// db.products.insertOne(
//    {city:'pune',gender:'f'}
// );

//db.products.find();

// ------------------ update -----------------
// update products set quantity=10 where name="chair";
//db.products.updateOne({name:'chair'},{$set:{quantity:10}});
//db.products.find();

//update products set price=250 where name="chair";
// db.products.updateOne({name:'chair'},
//                       {$set:{price:250},$currentDate:{lastModifieddate:true}});

// db.products.find();

// ------------------- delete --------------------------
// delete from products where gender=f;
//db.products.deleteOne({gender:'f'});
//db.products.find();

//deleting based on Id
// first copy the id of the product that you want to delete
//65d5d7ce03513f2b6ff2e9af
//db.products.deleteOne({_id:ObjectId('65d5d7ce03513f2b6ff2e9af')});
//db.products.find();

// ---------------- like ---------------------
//select * from products where name like 'i%';
//db.products.find({name:/^i/});

//select * from products where name like '%ok';
//db.products.find({name:/ok$/});

//select * from products where name like '%o%';
//db.products.find({name:/o/});

// -------------- in oprator --------------------
//select * from products where name quantity in(10,5);
// db.products.find(
//    {quantity:{$in:[10,5]}}
// );


// -------------- comparision oprator --------------------
// db.products.find(
//    {quantity:{$gt:5}}
// );

//------------logical and operator ------------------
//select * from products where name quantity>10 and price>100;
// db.products.find(
//    {quantity:{$gt:10},price:{$gt:100}}  
// );


//select * from products where name like '%ok' and quantity>10;
// db.products.find(
//    {quantity:{$gt:10} , name:/ok$/}  
// );

//------------logical or operator ------------------
// db.products.find(
//    { 
//       $or:
//       [
         
//             {quantity:{$gt:10}},
//             {price:{$gt:100}}   
//       ]
//    }   
// );


//-----------------working with array -----------------------
//exact match + order match + quantity match
// db.products.find(
//    {colors:['red','black']}
//    );

// db.products.find(
//       {colors:['black','red']}
//       );

//exact match + order does not match
// db.products.find(
//       {colors: {$all:['black','red']}}
// );

// db.products.find(
//    {colors: {$in:['black','red']}}
// );

// db.products.find(
//    {colors: 'yellow'}
// );

// db.products.find(
//    {colors: {$size: 3}}
// );

//getting all products whose array size (colors array size) is less than or equal to 2
// db.products.find(
//    {$expr : {$lte : [ {$size:"$colors"} ,2 ] } }
// )


//object filtration
//db.products.find();
//exact match
// db.products.find(
//   {
//    dimension: 
//    {
//       "w": 10,
//       "h": 20,
//       "unit": "cm"
//     }
//   }
// )

//products whose unit is inches
// db.products.find(
//    {
//     "dimension.unit":"in"
//    }
//  )

//products whos h>15
// db.products.find(
//    {
//     "dimension.h":{$gt:15}
//    }
//  )

 //products whos h>15 and unit=in
//  db.products.find(
//    {
//     "dimension.h":{$gt:15},
//     "dimension.unit":"in"
//    }
//  )



//-----------projections------------
//inclusion or exclusion of fields
//1 to inclusion, 0 for exclusion
//id is by default included
//we cant do inclusion and exlussion at time except for _id

//db.products.find({},{price:1});

//db.products.find({},{price:1,quantity:1});

//db.products.find({},{price:1,_id:0});

//db.products.find({},{price:1,quantity:0}); ERROR

//-----------count ---------------------------
//db.products.find().count()
//db.products.find({price:{$gt:100}}).count()

//-------------sorting----------------
//db.products.find().sort({price:1})
//db.products.find().sort({price:-1})

//asc order based on height
//db.products.find().sort({"dimension.h":1})

//------------------limit-----------
//db.products.find().limit(2);
//find product with highest price
//db.products.find().sort({price:-1}).limit(1);

//---------------skip----------
//db.products.find().skip(1);

//find product with 2nd highest price
//db.products.find().sort({price:-1}).skip(1).limit(1);

//---------------distinct--------------
db.products.distinct("quantity");


// data=db.products.distinct("quantity")
// print(data.length)








