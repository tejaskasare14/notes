import './Card.css'
const employee=[
   {
      "name":"Raj",
      "phone":"8458963254",
      "fb_url":"https://www.facebook.com/",
      "profile_pic":"http://localhost:3000/images/person.jfif"
   },
   {
      "name":"Aniket",
      "phone":"7856985425",
      "fb_url":"https://www.facebook.com/",
      "profile_pic":"http://localhost:3000/images/person.jfif"
   }
]
function Card()
{
   let profile = employee[1]
   return(
      <>
         <div className="card">
            <div className="card-items">
               <img src={profile.profile_pic} alt=""/>
               <div className="card-text">
                  <p>{profile.name}</p>
                  <p>{profile.phone}</p>
                  <a href={profile.fb_url}>Facebook Profile</a>
               </div>
            </div>
      </div>
      </>
   )
}

export default Card