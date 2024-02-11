use('amazon')

//----------------- LIKE operator-------------------------
//select * from products where name like 'i%'
//name starts with i
//db.products.find({name: /^i/})

//select * from products where name like '%book'
//name ends with book
//db.products.find({name: /book$/})

//select * from products where name like 'e'
//e anywhere in name
//db.products.find({name: /e/})


// ------------------ IN operator ------------------
//select * from products where quantity in(10,5);
// db.products.find(
//    {
//       quantity:
//             {
//                $in:[10,5]
//             }
//    })

//---------------- comparision operator ------------
//select * from products where quantity>10;
// db.products.find(
//    {
//       quantity:
//             {
//                //$gt:10
//                //$gte:10
//                //$lt:10
//                $lte:10
//             }
//    })

//-------------------- logcal and ----------------------
//select * from products where price>100 and quantity>5;
// db.products.find(
//    {
//       price:{ $gt:100},
//       quantity:{ $gt:5}
//    })

//select * from products where name like '%book' and price>100
//select * from products where name like '%book' and price>=100
// db.products.find(
//    {
//       name:/book$/,
//       //price:{ $gt:100}
//       price:{ $gte:100}
//    })

// -------------------- logical or -------------------------
//select * from products where price>100 or quantity>5;

// db.products.find(
//    {
//       $or:
//       [
//          {
//             price:{$gt:100}
//          },
//          {
//             quantity:{$gt:5}
//          }
//       ]
//    }
// )

// --------------- combinatation of and and or ------
//select * from products where name like 'p%' and (price>100 or quantity>5);
// db.products.find(
//    {
//       name :/^p/,
//       $or:
//       [
//          {
//             price:{$gt:100}
//          },
//          {
//             quantity:{$gt:5}
//          }
//       ]
//    }
// )



