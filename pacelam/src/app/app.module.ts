import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppComponent } from './app.component';
import { ClientComponent } from './client/client.component';
import { PaymentComponent } from './payment/payment.component';
import { StatusDirective } from './status.directive';
import { MapComponent } from './map/map.component';
import {NgbModule} from '@ng-bootstrap/ng-bootstrap';
import { LoginComponent } from './login/login.component';
import { ModalComponent } from './modal/modal.component';
import { WelcomeComponent } from './welcome/welcome.component';
import { HttpClientModule } from '@angular/common/http';
import {ReactiveFormsModule} from "@angular/forms";
import {ApiService} from "./api.service";
import { LoginmodalComponent } from './loginmodal/loginmodal.component';
import { ProfileComponent } from './profile/profile.component';
import {ModalService} from "./modal.service";
import { AppRoutingModule } from './app-routing.module';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { AgmCoreModule } from '@agm/core';


@NgModule({
  declarations: [
    AppComponent,
    ClientComponent,
    PaymentComponent,
    StatusDirective,
    MapComponent,
    LoginComponent,
    ModalComponent,
    WelcomeComponent,
    LoginmodalComponent,
    ProfileComponent
  ],
  imports: [
    BrowserModule,
    NgbModule.forRoot(),
    HttpClientModule,
    ReactiveFormsModule,
    AppRoutingModule,
    BrowserAnimationsModule,

     AgmCoreModule.forRoot({
      apiKey: 'AIzaSyC3fiie1AoGkZxnfh4kdgnr0V2rS2BA2pY'
    }),
  ],
  providers: [ApiService, ModalService],
  bootstrap: [AppComponent]
})
export class AppModule { }
