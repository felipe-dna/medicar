import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { LoginComponent } from './pages/login/login.component';
import { AuthGuard } from './shared/auth.guard';
import { LogoutComponent } from './pages/logout/logout.component';

const routes: Routes = [
  {
    path: '',
    component: HomeComponent,
    canActivate: [AuthGuard]
  },
  {
    path: '',
    children: [
      {
        path: 'login',
        component: LoginComponent,
      },
      {
        path: 'logout',
        component: LogoutComponent
      }
    ]
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
