import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../shared/service/api.service';
import { Appointment } from '../../shared/models/Appointment.model';
import { MatDialog } from '@angular/material/dialog';
import { AppointmentFormComponent} from './components/appointment-form/appointment-form.component';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})

export class HomeComponent implements OnInit {
  public userName: string;
  public appointmentList: Appointment[];
  displayedColumns: string[] = ['ESPECIALIDADE', 'PROFISSIONAL', 'DATA', 'HORA'];
  speciality: string;
  doctor: string;
  date: string;
  time: string;

  constructor(
    public apiService: ApiService,
    public appointmentDialog: MatDialog,
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
      this.doctor = result;
    });
  }

  ngOnInit(): void {
    this.getAppointments();
    this.userName = window.localStorage.getItem('userName');
  }

  removeAppointment(appointmentId): void {
    this.apiService.deleteAppointment(appointmentId).subscribe(() => {
      this.appointmentList = this.appointmentList.filter(value => value.id !== appointmentId);
    });
  }

  getAppointments(): void {
    this.apiService.getMedicalAppointments().subscribe(data => this.appointmentList = data);
  }
}
