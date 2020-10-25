import {Component, Inject, OnInit} from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import {ApiService} from '../../../../shared/service/api.service';
import {Speciality} from '../../../../shared/models/Appointment.model';

export interface AppointmentData {
  speciality: string;
  doctor: string;
  date: string;
  time: string;
}

@Component({
  selector: 'app-appointment-form',
  templateUrl: './appointment-form.component.html',
  styleUrls: ['./appointment-form.component.css']
})
export class AppointmentFormComponent implements OnInit {
  specialties: Speciality[];

  constructor(
    public apiService: ApiService,
    public dialogRef: MatDialogRef<AppointmentFormComponent>,
    @Inject(MAT_DIALOG_DATA) public appointmentData: AppointmentData
  ) { }

  ngOnInit(): void {
    this.getFormData();
  }

  onNoClick(): void {
    this.dialogRef.close();
  }

  // tslint:disable-next-line:typedef
  getFormData() {
    this.apiService.getMedicalSpecialties().subscribe(data => this.specialties = data);
  }
}
