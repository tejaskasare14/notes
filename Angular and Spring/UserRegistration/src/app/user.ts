export interface UserInterface
{
         _embedded: 
         {
            users: 
            [
               {
                     name: string,
                     age: number,
                     phone: string,
               }
            ]
        }
}

export interface User{
   name: string,
                     age: number,
                     phone: string,
}