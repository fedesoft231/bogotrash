import { NgModule } from '@angular/core';
import { IonicPageModule } from 'ionic-angular';
import { WasteinfoPage } from './wasteinfo';

@NgModule({
  declarations: [
    WasteinfoPage,
  ],
  imports: [
    IonicPageModule.forChild(WasteinfoPage),
  ],
})
export class WasteinfoPageModule {}
