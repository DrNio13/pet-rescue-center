import { Component, OnInit, Input } from '@angular/core';
import { ModalController } from '@ionic/angular';
import { AuthService } from 'src/app/services/auth.service';
import { PetsService } from '../../../services/pets.service';

@Component({
  selector: 'app-pet-form',
  templateUrl: './pet-form.component.html',
  styleUrls: ['./pet-form.component.scss'],
})
export class PetFormComponent implements OnInit {
  @Input() pet: any;
  @Input() isNew: boolean;
  email: string;

  constructor(
    public auth: AuthService,
    private modalCtrl: ModalController,
    private petService: PetsService
  ) { }

  ngOnInit() {
    if (this.isNew) {
      this.pet = {
        id: -1,
        name: '',
        breed: '',
        description: '',
        seeking_owner: true
      };

    }
  }

  customTrackBy(index: number, obj: any): any {
    return index;
  }

  closeModal() {
    this.modalCtrl.dismiss();
  }

  saveClicked() {
    this.petService.savePet(this.pet);
    this.closeModal();
  }

  deleteClicked() {
    this.petService.deletePet(this.pet).subscribe((res) => {
      window.location.href = window.location.origin;
    });
  }

  enquiryClicked() {
    this.petService.enquiryForPet({ ...this.pet, email: this.email }).subscribe((res) => {
      window.location.href = window.location.origin;
    });
  }
}
