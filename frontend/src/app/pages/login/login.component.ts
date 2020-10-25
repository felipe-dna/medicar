import { Component, OnInit } from '@angular/core';
import {Router} from '@angular/router';
import {ApiService} from '../../shared/service/api.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  public hidePassword = true;
  public login = {
    email: '',
    password: ''
  };

  constructor(
    public apiService: ApiService,
    private router: Router,
  ) { }

  ngOnInit(): void {
  }

  onSubmit(event): void {
    event.preventDefault();
    this.authenticateUser(this.login);
  }

  getUserData(): void {
    this.apiService.getUserData().subscribe(data => {
      window.localStorage.setItem('userName', data[0].name);
    });
  }

  authenticateUser(credentials): void {
    this.apiService.authenticateUser(credentials).subscribe(data => {
      this.getUserData();
      window.localStorage.setItem('token', data.token);
      this.router.navigate(['']);
    },
      error => { console.log(error); }
    );
  }
}
