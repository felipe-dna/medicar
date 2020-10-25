import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../shared/service/api.service';
import { Appointment } from '../../shared/models/Appointment.model';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})

export class HomeComponent implements OnInit {
  appointmentList: Appointment[];
  displayedColumns: string[] = ['ESPECIALIDADE', 'PROFISSIONAL', 'DATA', 'HORA'];

  constructor(
    public apiService: ApiService
  ) {}

  ngOnInit(): void {
    this.getAppointments();
  }

  // tslint:disable-next-line:typedef
  getAppointments() {
    this.apiService.getMedicalAppointments().subscribe(data => {
      console.log(data);
      this.appointmentList = data;
    });
  }
}
