# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import friend_service.friend_service_pb2 as friend__service__pb2


class FriendServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.add_friend = channel.unary_unary(
                '/friend_service.FriendService/add_friend',
                request_serializer=friend__service__pb2.AddFriendRequest.SerializeToString,
                response_deserializer=friend__service__pb2.AddFriendResponse.FromString,
                )
        self.get_friends = channel.unary_unary(
                '/friend_service.FriendService/get_friends',
                request_serializer=friend__service__pb2.GetFriendsRequest.SerializeToString,
                response_deserializer=friend__service__pb2.GetFriendsResponse.FromString,
                )
        self.remove_friend = channel.unary_unary(
                '/friend_service.FriendService/remove_friend',
                request_serializer=friend__service__pb2.RemoveFriendRequest.SerializeToString,
                response_deserializer=friend__service__pb2.RemoveFriendResponse.FromString,
                )
        self.set_invite = channel.unary_unary(
                '/friend_service.FriendService/set_invite',
                request_serializer=friend__service__pb2.SetInviteRequest.SerializeToString,
                response_deserializer=friend__service__pb2.SetInviteResponse.FromString,
                )
        self.get_invites = channel.unary_unary(
                '/friend_service.FriendService/get_invites',
                request_serializer=friend__service__pb2.GetInvitesRequest.SerializeToString,
                response_deserializer=friend__service__pb2.GetInvitesResponse.FromString,
                )
        self.update_invite_status = channel.unary_unary(
                '/friend_service.FriendService/update_invite_status',
                request_serializer=friend__service__pb2.UpdateInviteStatusRequest.SerializeToString,
                response_deserializer=friend__service__pb2.UpdateInviteStatusResponse.FromString,
                )


class FriendServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def add_friend(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_friends(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def remove_friend(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def set_invite(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_invites(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update_invite_status(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FriendServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'add_friend': grpc.unary_unary_rpc_method_handler(
                    servicer.add_friend,
                    request_deserializer=friend__service__pb2.AddFriendRequest.FromString,
                    response_serializer=friend__service__pb2.AddFriendResponse.SerializeToString,
            ),
            'get_friends': grpc.unary_unary_rpc_method_handler(
                    servicer.get_friends,
                    request_deserializer=friend__service__pb2.GetFriendsRequest.FromString,
                    response_serializer=friend__service__pb2.GetFriendsResponse.SerializeToString,
            ),
            'remove_friend': grpc.unary_unary_rpc_method_handler(
                    servicer.remove_friend,
                    request_deserializer=friend__service__pb2.RemoveFriendRequest.FromString,
                    response_serializer=friend__service__pb2.RemoveFriendResponse.SerializeToString,
            ),
            'set_invite': grpc.unary_unary_rpc_method_handler(
                    servicer.set_invite,
                    request_deserializer=friend__service__pb2.SetInviteRequest.FromString,
                    response_serializer=friend__service__pb2.SetInviteResponse.SerializeToString,
            ),
            'get_invites': grpc.unary_unary_rpc_method_handler(
                    servicer.get_invites,
                    request_deserializer=friend__service__pb2.GetInvitesRequest.FromString,
                    response_serializer=friend__service__pb2.GetInvitesResponse.SerializeToString,
            ),
            'update_invite_status': grpc.unary_unary_rpc_method_handler(
                    servicer.update_invite_status,
                    request_deserializer=friend__service__pb2.UpdateInviteStatusRequest.FromString,
                    response_serializer=friend__service__pb2.UpdateInviteStatusResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'friend_service.FriendService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FriendService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def add_friend(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/friend_service.FriendService/add_friend',
            friend__service__pb2.AddFriendRequest.SerializeToString,
            friend__service__pb2.AddFriendResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_friends(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/friend_service.FriendService/get_friends',
            friend__service__pb2.GetFriendsRequest.SerializeToString,
            friend__service__pb2.GetFriendsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def remove_friend(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/friend_service.FriendService/remove_friend',
            friend__service__pb2.RemoveFriendRequest.SerializeToString,
            friend__service__pb2.RemoveFriendResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def set_invite(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/friend_service.FriendService/set_invite',
            friend__service__pb2.SetInviteRequest.SerializeToString,
            friend__service__pb2.SetInviteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_invites(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/friend_service.FriendService/get_invites',
            friend__service__pb2.GetInvitesRequest.SerializeToString,
            friend__service__pb2.GetInvitesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def update_invite_status(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/friend_service.FriendService/update_invite_status',
            friend__service__pb2.UpdateInviteStatusRequest.SerializeToString,
            friend__service__pb2.UpdateInviteStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
