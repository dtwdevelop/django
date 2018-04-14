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


@NgModule({
  declarations: [
    AppComponent,
    ClientComponent,
    PaymentComponent,
    StatusDirective,
    MapComponent,
    LoginComponent,
    ModalComponent
  ],
  imports: [
    BrowserModule,
    NgbModule.forRoot()
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
