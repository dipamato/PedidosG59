import {injectable, /* inject, */ BindingScope} from '@loopback/core';
const generador=require("generate-password");
const crypoJS=require("crypto-js");

@injectable({scope: BindingScope.TRANSIENT})
export class AutenticacionService {
  constructor(/* Add @inject to inject parameters */) {}

  /*
   * Add service methods here
   */
  GenerarPassword(){
    let password= generador.generate({
      length: 8,
      numbers:true
    });
    return password;
  }

  EncriptarPassword(password:string){
    let passwordE=crypoJS.MD5(password);
    return passwordE;
  }
}
