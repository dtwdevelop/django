import { Component ,Output } from '@angular/core';
import {NgbModal,NgbModalRef} from "@ng-bootstrap/ng-bootstrap";
import {ModalService} from "./modal.service";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'app';
   constructor(private modal:ModalService) {
    }
    open(content) {
    this.modal.open(content)
  }
  onClose(event){

   this.modal.onClose(event)
  }
}
