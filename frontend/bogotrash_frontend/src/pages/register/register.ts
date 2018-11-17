import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { RestProvider } from '../../providers/rest/rest';
import { HomePage } from '../home/home';

/**
 * Generated class for the RegisterPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-register',
  templateUrl: 'register.html',
})
export class RegisterPage {

  nombre: String;
  apellido: String;
  cedula: String;
  correo: String;
  username: String;
  password: String;

  constructor(public navCtrl: NavController, public navParams: NavParams, public restProvider: RestProvider) {
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad RegistroPage');
  }

  registrarUsuario() {
    var data = {
      'nombre': this.nombre,
      'apellido': this.apellido,
      'cedula': this.cedula,
      'correo': this.username,
      'username': this.username,
      'password': this.password,
    }

    this.restProvider.registrarUsuario(data).then(Response => {
      var data = { 'username': this.username, 'password': this.password };
      this.restProvider.login(data).then((data: any) => {
        window.localStorage['token'] = data.key;
        this.navCtrl.push(HomePage);
      }, (err) => {
        console.log(err);
      });
    }, err => {
      console.log(err)
    });
  }

}
