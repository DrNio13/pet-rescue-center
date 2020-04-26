import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../services/auth.service';
import { PetsService } from '../../services/pets.service';

@Component({
  selector: 'app-enquiries-page',
  templateUrl: './enquiries-page.page.html',
  styleUrls: ['./enquiries-page.page.scss'],
})
export class EnquiriesPage implements OnInit {
  public enquirie$: any;

  constructor(public auth: AuthService, private petService: PetsService) { }

  ngOnInit() {
    this.enquirie$ = this.petService.getEnquiriesForPets();
  }

}
