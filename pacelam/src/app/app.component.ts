import { Component ,Output } from '@angular/core';
import {NgbModal,NgbModalRef} from "@ng-bootstrap/ng-bootstrap";



@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'app';
   modalReference:NgbModalRef


 constructor(private modalService:NgbModal) {}
  open(content) {

     this.modalReference  = this.modalService.open(content);
     this.modalReference.result.then((result) => {

    }, (reason) => {

    });
  }
  onClose(event){

    this.modalReference.close()
  }




}
