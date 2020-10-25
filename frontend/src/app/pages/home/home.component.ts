import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../shared/service/api.service';
import { Appointment, Speciality } from '../../shared/models/Appointment.model';
import { MatDialog } from '@angular/material/dialog';
import { AppointmentFormComponent } from './components/appointment-form/appointment-form.component';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})

export class HomeComponent implements OnInit {
  appointmentList: Appointment[];
  displayedColumns: string[] = ['ESPECIALIDADE', 'PROFISSIONAL', 'DATA', 'HORA'];
  speciality: string;
  doctor: string;
  date: string;
  time: string;

  constructor(
    public apiService: ApiService,
    public appointmentDialog: MatDialog
  ) {}

  openDialog(): void {
    const dialogRef = this.appointmentDialog.open(AppointmentFormComponent, {
      id: 'appointment-form-dialog',
      width: '480px',
      height: '420px',
      data: {
        speciality: this.speciality,
        doctor: this.doctor,
        date: this.date,
        time: this.time
      }
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log('The dialog was closed');
      this.doctor = result;
    });
  }

  ngOnInit(): void {
    this.getAppointments();
  }

  // tslint:disable-next-line:typedef
  getAppointments() {
    this.apiService.getMedicalAppointments().subscribe(data => this.appointmentList = data);
  }
}
