import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { RestProvider } from '../../providers/rest/rest';
import { HomePage } from '../home/home';
import { RegisterPage } from '../register/register';

/**
 * Generated class for the LoginPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-login',
  templateUrl: 'login.html',
})
export class LoginPage {

  usuario: String;
  clave: String;

  constructor(public navCtrl: NavController, public navParams: NavParams, public restProvider: RestProvider) {
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad LoginPage');
    if(window.localStorage['token']){
      this.navCtrl.setRoot(HomePage);
    }
  }

  register(){
    this.navCtrl.push(RegisterPage);
  }

  iniciarSesion() {
    var data = { 'username':this.usuario, 'password':this.clave };
    this.restProvider.login(data).then((data:any) => {
      window.localStorage['token'] = data.key;
      this.navCtrl.push(HomePage);
    }, (err) => {
    console.log(err);
    });

    console.log(this.usuario);
    console.log(this.clave);
  }

}
