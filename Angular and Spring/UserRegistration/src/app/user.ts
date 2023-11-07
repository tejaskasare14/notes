export interface UserInterface
{
   id:number,      
   name: string,
   age: number,
   phone: string,
}

export class User{    
   name!: string
   age!: number
   phone!: string
}