import { Component, OnInit } from '@angular/core';
import { PetsService } from '../../services/pets.service';
import { ModalController } from '@ionic/angular';

import { AuthService } from 'src/app/services/auth.service';
import { PetFormComponent } from './pet-form/pet-form.component';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-pets',
  templateUrl: './pets.page.html',
  styleUrls: ['./pets.page.scss'],
})
export class PetsPage implements OnInit {
  Object = Object;
  pet$: Observable<any>;

  constructor(
    private auth: AuthService,
    private modalCtrl: ModalController,
    public petsService: PetsService
  ) { }

  ngOnInit() {
    this.pet$ = this.petsService.getPets();
  }

  async openForm(activePet: any = null) {

    if (!this.auth.can('get:pets-details')) {
      return;
    }

    const modal = await this.modalCtrl.create({
      component: PetFormComponent,
      componentProps: { pet: activePet, isNew: !activePet }
    });

    modal.present();
  }

}
