use('amazon')

//---------------- exact quantity match and order matters --------------
// db.products.find(
//    {
//       colors:['red','black']
//    }
// )

// db.products.find(
//    {
//       colors:['black','red']
//    }
// )

//------ exact match but order dosnt matter
// db.products.find(
//    {
//       colors:{$all :['black','red']}
//    }
// )

// no exact match no order match
//either black or red or both
// db.products.find(
//    {
//       colors:{$in :['black','red']}
//    }
// )

//-------single match in array
//all products who have blue color
// db.products.find(
//    {
//       colors:'blue'
//    }
// )

//--------- find based on array size
// db.products.find(
//    {
//       colors:{
//          $size:3
//       }
//    }
// )

