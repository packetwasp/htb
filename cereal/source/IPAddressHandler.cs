using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Http;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Threading.Tasks;

namespace Cereal
{
    public class IPAddressHandler : AuthorizationHandler<IPRequirement>
    {
        private readonly IHttpContextAccessor httpContextAccessor;

        public IPAddressHandler(IHttpContextAccessor httpContextAccessor)
        {
            this.httpContextAccessor = httpContextAccessor;
        }

        protected override Task HandleRequirementAsync(AuthorizationHandlerContext context, IPRequirement requirement)
        {
            var httpContext = httpContextAccessor.HttpContext;
            var ipAddress = httpContext.Connection.RemoteIpAddress;

            Console.WriteLine("IP: "+ipAddress);
            List<string> whiteListIPList = requirement.Whitelist;
            var isInwhiteListIPList = whiteListIPList
                .Where(a => IPAddress.Parse(a)
                .Equals(ipAddress))
                .Any();
            if (isInwhiteListIPList)
            {
                Console.WriteLine("SUCCESS");
                context.Succeed(requirement);
            }
            return Task.CompletedTask;
        }
    }
}
