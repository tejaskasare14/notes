let select_from = document.getElementById("select_from")
let convert_to = document.getElementById("convert_to")
let btn = document.getElementById("btn")
let input_currency = document.getElementById("input_currency")
let output_currency = document.getElementById("output_currency")
let from_country_name  = document.getElementById("from_country_name")
let to_country_name = document.getElementById("to_country_name")

fetch("https://api.frankfurter.app/currencies")
.then((response) => {
    response.json()
   .then((actual_curreny_data) => {
      console.log(actual_curreny_data)
      let currency_code = Object.keys(actual_curreny_data)
      let currency_name = Object.values(actual_curreny_data)
      console.log(currency_code);
      console.log(currency_name);

      //select_from.innerHTML = `<option>${currency_code}</option>`
      for(let currency of currency_code)
      {
         select_from.innerHTML += `<option>${currency}</option>`
         convert_to.innerHTML += `<option>${currency}</option>`
      }
   })
   .catch()
})
.catch(() => {})


btn.addEventListener("click",()=>{

   //alert(input_currency.value)
   let input = input_currency.value
   console.log(select_from.value);
   console.log(convert_to.value);
   const host = 'api.frankfurter.app';
   fetch(`https://${host}/latest?amount=${input}&from=${select_from.value}&to=${convert_to.value}`)
     .then(resp => resp.json())
     .then((data) => {
      let converted_amount = Object.entries(data.rates)[0];
      console.log(converted_amount[1]);
      output_currency.value = converted_amount[1]
     });





})