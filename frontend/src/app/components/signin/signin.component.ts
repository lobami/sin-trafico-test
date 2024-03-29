import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../services/auth.service'
import { Router } from '@angular/router'

@Component({
  selector: 'app-signin',
  templateUrl: './signin.component.html',
  styleUrls: ['./signin.component.css']
})
export class SigninComponent implements OnInit {
  user = {};

  constructor(
    private authService: AuthService,
    private router: Router
  ) { }

  ngOnInit() {
  }

  signIn() {
    this.authService.signInUser(this.user)
      .subscribe(
        res => {
          console.log('me estoy logueando')
          console.log(res);
          localStorage.setItem('token', res.token);
          localStorage.setItem('user_id', res.user_id);
          this.router.navigate(['/units']);
        },
        err => console.log(err)
      )
  }

}
