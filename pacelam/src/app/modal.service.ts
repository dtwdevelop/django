import { Injectable } from '@angular/core';
import {NgbModal,NgbModalRef} from "@ng-bootstrap/ng-bootstrap";
@Injectable()
export class ModalService {
   modalReference:NgbModalRef;

  constructor(private modalService: NgbModal) {

  }
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
