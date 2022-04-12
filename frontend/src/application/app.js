/**
 * A modern blog web app
 *
 * Created by Nguyen Truong Thinh
 * Contact me: nguyentruongthinhvn2020@gmail.com || +84393280504
 */

import "../styles/index.scss";

import "bootstrap/dist/js/bootstrap.bundle";
import {setupComment} from "../components/comment";

window.BeeBlog = {
  setupComment: setupComment
};

window.document.addEventListener("DOMContentLoaded", function () {
  window.console.log("dom ready");
});
