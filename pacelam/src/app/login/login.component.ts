import { Component, OnInit } from '@angular/core';
import {NgbModal,NgbModalRef} from "@ng-bootstrap/ng-bootstrap";
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
   modalReference:NgbModalRef;

  constructor(private modalService: NgbModal) {}

  open(content) {
     this.modalReference  = this.modalService.open(content);
     this.modalReference.result.then((result) => {

    }, (reason) => {

    });
  }
  onClose(event){

    this.modalReference.close()
  }

  ngOnInit() {
  }

}
