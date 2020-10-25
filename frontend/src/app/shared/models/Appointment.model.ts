export class AppointmentDoctorSpeciality {
  id: string;
  name: string
}

export class AppointmentDoctor {
  id: string;
  name: string;
  crm: number;
  speciality: AppointmentDoctorSpeciality
}

export class Appointment {
  id: string;
  time: string;
  doctor: AppointmentDoctor
}
