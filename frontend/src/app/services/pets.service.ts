import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { AuthService } from './auth.service';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class PetsService {
  public items: { [key: number]: any } = {};
  public url = environment.apiServerUrl;

  constructor(private auth: AuthService, private http: HttpClient) { }

  getHeaders() {
    const header = {
      headers: new HttpHeaders()
        .set('Authorization', `Bearer ${this.auth.activeJWT()}`)
    };
    return header;
  }

  getPets() {
    if (this.auth.can('get:pets-detail')) {
      this.http.get(this.url + '/pets-detail', this.getHeaders())
        .subscribe((res: any) => {
          this.petsToItems(res.pets);
          console.log(res);
        });
    } else {
      this.http.get(this.url + '/pets', this.getHeaders())
        .subscribe((res: any) => {
          this.petsToItems(res.pets);
          console.log(res);
        });
    }

  }

  savePet(pet: any) {
    if (pet.id >= 0) { // patch
      this.http.patch(this.url + '/pets/' + pet.id, pet, this.getHeaders())
        .subscribe((res: any) => {
          if (res.success) {
            this.petsToItems(res.pets);
          }
        });
    } else { // insert
      this.http.post(this.url + '/pets', pet, this.getHeaders())
        .subscribe((res: any) => {
          if (res.success) {
            this.petsToItems(res.pets);
          }
        });
    }

  }

  deletePet(pet: any) {
    delete this.items[pet.id];
    this.http.delete(this.url + '/pets/' + pet.id, this.getHeaders())
      .subscribe((res: any) => {

      });
  }

  petsToItems(pets: Array<any>) {
    for (const pet of pets) {
      this.items[pet.id] = pet;
    }
  }
}
