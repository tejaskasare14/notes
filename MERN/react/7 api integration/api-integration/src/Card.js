import './Card.css'


function Card(props)
{
   // let profile = props.employee_data
   let profile = props
   
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