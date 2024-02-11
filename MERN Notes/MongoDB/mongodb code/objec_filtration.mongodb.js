use('amazon')

// ----------------- exact mactch ---------------------
// db.products.find(
//    {
//       dimension: {
//          w: 10,
//          h: 20,
//          unit: "cm"
//        }
//    }
// )

// ---- products whos dimensions are in inches ---------
// db.products.find(
//    {
//      'dimension.unit':'in'
//    }
// )

// products whose dimension.h > 15
// db.products.find(
//    {
//      'dimension.h':{$gt:15}
//    }
// )

// dimension.h> 15 and dimension.w>30
// db.products.find(
//    {
//      'dimension.h':{$gt:15},
//      'dimension.w':{$gt:30},
//    }
// )
