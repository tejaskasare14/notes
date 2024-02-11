use('amazon')
//--------------- PROJECTION -----------------
//projection - inclusion

//select price from products;
//db.products.find({},{price:1})
//_id is by default selected

//select price,quantity from products;
//_id is by default selected so add 0 to exclude
// db.products.find({},
//    {
//       price:1,
//       quantity:1,
//       _id:0
//    })

//projection - exclusion
// do not show price
// db.products.find({},
//    {
//       price:0,
//    })

//we cant include or exclude fields at a time
// db.products.find({},
//    {
//       price:0,
//       quantity:1
//    })

//-------------------COUNT ----------------------------
//db.products.find().count()

//count based on condition
// db.products.find(
//    {
//       quantity:5
//    }
// ).count()

// -----------------------SORTING ---------------
//sort : asc
//db.products.find().sort({quantity:1})

//sort : desc
//db.products.find().sort({quantity:-1})

//sort : in object
//dimension height in asc order
//db.products.find().sort({'dimension.h':1})

//dimension height in desc order
//db.products.find().sort({'dimension.h':-1})

// ---------------------- LIMIT ------------------
//get top 2 records
//db.products.find().limit(2)

//sorting and limit
//db.products.find().sort({quantity:-1}).limit(2)

//-------------------- SKIP -------------
//db.products.find().skip(2)
//db.products.find().skip(2).limit(2)

//product with highest price
//db.products.find().sort({price:-1})
//db.products.find().sort({price:-1}).limit(1)

//product with second highest
//db.products.find().sort({price:-1}).skip(1).limit(1)

db.products.find().pretty()