import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent implements OnInit {
  public hidePassword = true;
  public hideConfirmPassword = true;
  public userSignupData = {
    email: '',
    name: '',
    password: '',
    confirmPassword: ''
  };

  constructor() { }

  ngOnInit(): void {
  }

  async submitForm(event): Promise<void> {
    event.preventDefault();
  }
}
