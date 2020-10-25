export class Speciality {
  id: string;
  name: string;
}

export class Doctor {
  id: string;
  name: string;
  speciality: Speciality;
}

export class Appointment {
  id: string;
  time: string;
}
