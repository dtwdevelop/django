import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, Routes } from '@angular/router';
import {ProfileComponent} from './profile/profile.component'
import {LoginComponent} from "./login/login.component";
import {MapComponent} from "./map/map.component";

const routes: Routes = [
  { path: '', redirectTo: '/login', pathMatch: 'full' },
  { path: 'send', component: MapComponent },
   { path: 'login', component: LoginComponent }

];
@NgModule({
  imports: [
    CommonModule,
    RouterModule.forRoot(routes)
  ],
  exports: [RouterModule]

})
export class AppRoutingModule {  }
