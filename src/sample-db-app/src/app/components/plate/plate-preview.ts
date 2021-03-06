import { Component, Input, ChangeDetectionStrategy } from '@angular/core';
import { MatrixPlate } from '../../models/plate';
import { Location } from '../../models/location';

@Component({
  selector: 'sdb-plate-preview',
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `
    <a [routerLink]="['/plate', id]">
      <md-card>
        <md-card-title-group>
          <md-card-title style="display: flex">
            <div style="width: 190px">
              <span>{{ uid }}</span>
            </div>
            <div style="flex-grow: 1">
              <span class="hidden-toggle"><md-icon>{{ visibile }}</md-icon></span>
            </div>
          </md-card-title>
          <md-card-subtitle>{{ plateLocation }}</md-card-subtitle>
        </md-card-title-group>
        <md-card-content>
          <p><span class="content"><small>Created: {{ created | date:'mediumDate' }}</small></span></p>
          <p><span class="content"><small>Last Updated: {{ last_updated | date:'mediumDate' }}</small></span></p>
          <p *ngIf="numTubes !== undefined"><span><small># Tubes: {{ numTubes }}</small></span></p>
        </md-card-content>
      </md-card>
    </a>
  `,
  styles: [`
    md-card {
      width: 200px;
      height: 135px;
      margin: 5px;
    }
    @media only screen and (max-width: 768px) {
      md-card {
        margin: 10px 0 !important;
      }
    }
    md-card:hover {
      box-shadow: 3px 3px 16px -2px rgba(0, 0, 0, .5);
    }
    md-card-title {
      margin-right: 10px;
      width: 100%;
    }
    md-card-title-group {
      margin: 0;
    }
    a {
      color: inherit;
      text-decoration: none;
    }
    img {
      width: 60px;
      min-width: 60px;
      margin-left: 5px;
    }
    md-card-content {
      margin-top: 10px;
      margin: 1px 0 0;
    }
    .content {
      display: inline-block;
      font-size: 13px;
    }
    md-card-footer {
      padding: 0 25px 25px;
    }
    .hidden-toggle {
      color: grey;
    }
  `]
})
export class MatrixPlatePreviewComponent {
  @Input() plate: MatrixPlate;
  @Input() location: Location;

  private _toggleClicked = false;

  get visibile() {
    return this.plate.hidden ? 'visibility_off' : 'visibility';
  }

  get id() {
    return this.plate.id;
  }

  get uid() {
    return this.plate.uid;
  }

  get created() {
    return this.plate.created;
  }

  get last_updated() {
    return this.plate.last_updated;
  }

  get plateLocation() {
    return this.location ? this.location.description : undefined;
  }

  get numTubes() {
    return this.plate ? this.plate.tubes.length : undefined;
  }

}
