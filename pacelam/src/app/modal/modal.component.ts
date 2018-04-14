import { Component, OnInit ,Output,EventEmitter} from '@angular/core';



@Component({
  selector: 'app-modal',
  templateUrl: './modal.component.html',
  styleUrls: ['./modal.component.css']
})
export class ModalComponent implements OnInit {

   @Output() onClose = new EventEmitter<boolean>();
    ngOnInit() {
  }


   close(d){

         this.onClose.emit(true)
   }

}
