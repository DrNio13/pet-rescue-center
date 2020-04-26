import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { TabsPage } from './tabs.page';

const routes: Routes = [
  {
    path: 'tabs',
    component: TabsPage,
    children: [
      { path: 'pets-page', loadChildren: '../pets-page/pets.page.module#PetsPageModule' },
      { path: 'user-page', loadChildren: '../user-page/user-page.module#UserPageModule' },
      { path: 'enquiries-page', loadChildren: '../enquiries-page/enquiries-page.module#EnquiriesPageModule' },
      {
        path: '',
        redirectTo: '/tabs/pets-page',
        pathMatch: 'full'
      }
    ]
  },
  {
    path: '',
    redirectTo: '/tabs/pets-page',
    pathMatch: 'full'
  }
];

@NgModule({
  imports: [
    RouterModule.forChild(routes)
  ],
  exports: [RouterModule]
})
export class TabsPageRoutingModule { }
