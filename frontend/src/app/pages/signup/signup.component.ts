import { Component, OnInit } from '@angular/core';
import {ApiService} from '../../shared/service/api.service';
import {Router} from '@angular/router';
import {RegisterUserBodyParameters} from '../../shared/models/Appointment.model';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent implements OnInit {
  public hidePassword = true;
  public hideConfirmPassword = true;
  public formValid = false;
  public userSignupData = {
    email: '',
    name: '',
    password: '',
    confirmPassword: ''
  };
  public userSignupFormInputStateControl = {
    email: null,
    name: null,
    password: null,
  };

  constructor(
    public apiService: ApiService,
    private router: Router,
  ) { }

  ngOnInit(): void {
  }

  validateFormOnChange(): void {
    this.formValid = this.userSignupData.email !== '' &&
      this.userSignupData.name !== '' &&
      this.userSignupData.password !== '' &&
      this.userSignupData.password === this.userSignupData.confirmPassword;

    if (
      (this.userSignupData.password !== '' && this.userSignupData.confirmPassword !== '') &&
      this.userSignupData.password !== this.userSignupData.confirmPassword
    ) {
      this.userSignupFormInputStateControl.password = 'As senhas são diferentes.';
    } else {
      this.userSignupFormInputStateControl.password = null;
    }
  }

  async validateRequiredParameters(): Promise<void> {
    if (this.userSignupData.name === '') {
      this.userSignupFormInputStateControl.name = 'O campo <strong>Nome</strong> é obrigatório';
    }

    if (this.userSignupData.email === '') {
      this.userSignupFormInputStateControl.name = 'O campo <strong>email</strong> é obrigatório';
    }

    if (this.userSignupData.password === '' || this.userSignupData.confirmPassword === '' ) {
      this.userSignupFormInputStateControl.password = 'O campo <strong>Nome</strong> é obrigatório';
    }
  }

  async resetErrors(): Promise<void> {
    this.userSignupFormInputStateControl = {
      email: null,
      name: null,
      password: null,
    };
  }

  async submitForm(event): Promise<void> {
    event.preventDefault();

    await this.resetErrors();
    await this.validateRequiredParameters();

    await this.registerUser({
      name: this.userSignupData.name,
      email: this.userSignupData.email,
      password: this.userSignupData.password
    });
  }

  async registerUser(bodyParmeters: RegisterUserBodyParameters): Promise<void> {
    this.apiService.registerUser(bodyParmeters)
      .subscribe(
        async data => this.router.navigate(['']),
        async error => this.userSignupFormInputStateControl = {...error.error});
  }
}
