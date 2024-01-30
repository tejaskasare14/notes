//collecting html tags using DOM
let select_from=document.getElementById('select_from')
let convert_to=document.getElementById('convert_to')
let btn=document.getElementById('btn')
let input_currency=document.getElementById('input_currency')
let output_currency=document.getElementById('output_currency')

fetch("https://api.frankfurter.app/currencies")
   .then(data => 
         {
            data.json()
               .then(actual_data => 
                        {
                           //displaying actual_data that we get after converting into json
                           //console.log(actual_data);

                           //since the actual_data is in Object format, lets separate out its keys and values
                           let currency_codes=Object.keys(actual_data)
                           let currency_names=Object.values(actual_data)
                           // console.log(currency_codes);
                           // console.log(currency_names);


                           //using for of loop to fetch data from array (currency_codes array)
                           for(currency_code of currency_codes)
                           {
                              // console.log(currency_code);
                              //creating option inside select tag in html
                              select_from.innerHTML += `<option>${currency_code}</option>`
                              convert_to.innerHTML += `<option>${currency_code}</option>`
                           }
                        })
               .catch(err => console.log("cant convert into json"))
         })
   .catch(err => { console.log("api is wrong, data not found"); })

   //handling button click and coverting currency
   btn.addEventListener("click",()=>
   {  
      //console.log("button is clicked");
      console.log(select_from.value);
      console.log(convert_to.value);
      console.log(input_currency.value);

      const host = 'api.frankfurter.app';
         fetch(`https://${host}/latest?amount=${input_currency.value}&from=${select_from.value}&to=${convert_to.value}`)
         .then(resp => resp.json())
         .then((data) => {
            console.log(data.rates);
            let result=Object.values(data.rates)
            console.log(result);
            console.log(result[0]);
            output_currency.value=result[0]
         });
   })                            